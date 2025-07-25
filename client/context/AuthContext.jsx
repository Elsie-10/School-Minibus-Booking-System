'use client';
import { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => { // this is what is exported in layout to wrap the whole project
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // const checkAuth = async () => {
  //   try {
  //     const res = await fetch('http://localhost:5000/auth/current_user', {
  //       credentials: 'include',
  //     });

  //     if (res.ok) {
  //       const userData = await res.json();
  //       setUser(userData);
  //     } else {
  //       setUser(null);
  //     }
  //   } catch (err) {
  //     setUser(null);
  //   } finally {
  //     setLoading(false);
  //   }
  // };

  const checkAuth = async () =>{
    try{
      const response = await axios.get('http://localhost:5000/auth/current_user',{
        withCredentials: true, // Include cookies in the request
      })
      if(response.status === 200){
        console.log('User data:', response.data);
        setUser(response.data);
      }else{
        setUser(null);
      }

    }catch(error){
      console.error('Error checking auth:', error);
      setUser(null);
    } finally {
      setLoading(false);
      }}
  useEffect(() => {
    checkAuth();
  }, []);

  const login = (userData) => {
    setUser(userData);
  };

  const logout = async () => {
    try {
      await fetch('http://localhost:5000/auth/logout', {
        method: 'POST',
        credentials: 'include',
      });
    } catch (err) {
      console.error('Logout error:', err);
    } finally {
      setUser(null);
    }
  };
// this is what is exported to the navbar
  return (
    <AuthContext.Provider value={{ user, login, logout, checkAuth, loading }}> 
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

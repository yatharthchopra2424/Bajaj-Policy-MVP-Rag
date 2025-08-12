import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import ChatBar from './components/ChatBar';
import Home from './pages/HomePage';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <div className="flex flex-col h-screen">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </main>
        <ChatBar />
      </div>
    </Router>
  );
}

export default App;

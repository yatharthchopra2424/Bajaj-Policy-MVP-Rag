import React from 'react';
import { NavLink } from 'react-router-dom';
import { Button } from './ui/Button';

export const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-black/30 backdrop-blur-lg">
      <div className="container mx-auto px-6 py-3 flex justify-between items-center">
        <NavLink to="/" className="text-2xl font-bold text-white">
          Documind
        </NavLink>
        <div className="hidden md:flex items-center space-x-8">
          <NavLink to="/#features" className="text-white hover:text-white transition-colors">Features</NavLink>
          <NavLink to="/#pricing" className="text-white hover:text-white transition-colors">Pricing</NavLink>
          <NavLink to="/marketplace" className="text-white hover:text-white transition-colors">Marketplace</NavLink>
        </div>
        <div className="flex items-center space-x-4">
          <Button variant="ghost" asChild>
            <NavLink to="/dashboard" className="text-white hover:text-white transition-colors">Dashboard</NavLink>
          </Button>
        </div>
      </div>
    </nav>
  );
};
import React from 'react';
import { NavLink } from 'react-router-dom';

export const Footer = () => {
  return (
    <footer className="bg-black/30 border-t border-[#FCD34D]/20">
      <div className="container mx-auto px-6 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-xl font-bold text-white mb-4">LexiPro</h3>
            <p className="text-gray-400">The future of legal technology.</p>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li><NavLink to="/#features" className="text-gray-400 hover:text-white">Features</NavLink></li>
              <li><NavLink to="/#pricing" className="text-gray-400 hover:text-white">Pricing</NavLink></li>
              <li><NavLink to="/marketplace" className="text-gray-400 hover:text-white">Marketplace</NavLink></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-4">Legal</h4>
            <ul className="space-y-2">
              <li><NavLink to="/privacy" className="text-gray-400 hover:text-white">Privacy Policy</NavLink></li>
              <li><NavLink to="/terms" className="text-gray-400 hover:text-white">Terms of Service</NavLink></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-4">Follow Us</h4>
            <div className="flex space-x-4">
              {/* Add social media links here */}
            </div>
          </div>
        </div>
        <div className="mt-12 text-center text-gray-500">
          <p>&copy; {new Date().getFullYear()} LexiPro. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};
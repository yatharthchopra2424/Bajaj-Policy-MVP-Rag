import React from 'react';
import MetricCard from '../components/MetricCard';
import ResponseChart from '../components/ResponseChart';
import Sidebar from '../components/Sidebar';

const Dashboard = () => {
  return (
    <div className="flex h-full bg-gradient-to-br from-black via-gray-900 to-[#1e1b4b]">
      <Sidebar />
      <div className="flex-grow p-8">
        <h1 className="text-3xl font-bold text-white mb-8">Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          <MetricCard title="Total Requests Given" value="150" />
          <MetricCard title="Average Response Time" value="2.5s" />
          <MetricCard title="Total Questions Answered" value="500" />
        </div>
        <div className="bg-black/60 p-6 rounded-lg shadow-md">
          <ResponseChart />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
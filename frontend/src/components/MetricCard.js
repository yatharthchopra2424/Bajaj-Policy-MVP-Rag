import React from 'react';

const MetricCard = ({ title, value }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-gray-600 text-sm font-medium">{title}</h2>
      <p className="text-3xl font-bold text-gray-800">{value}</p>
    </div>
  );
};

export default MetricCard;
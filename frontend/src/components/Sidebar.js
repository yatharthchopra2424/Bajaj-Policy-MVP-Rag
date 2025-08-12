import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Sidebar = () => {
  const [health, setHealth] = useState(null);
  const [cacheStats, setCacheStats] = useState(null);

  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const response = await axios.get('http://localhost:8000/health');
        setHealth(response.data);
      } catch (error) {
        console.error('Error fetching health:', error);
        setHealth({ status: 'unhealthy' });
      }
    };

    const fetchCacheStats = async () => {
      try {
        const response = await axios.get('http://localhost:8000/cache/stats');
        setCacheStats(response.data);
      } catch (error) {
        console.error('Error fetching cache stats:', error);
      }
    };

    fetchHealth();
    fetchCacheStats();
  }, []);

  return (
    <div className="w-64 bg-gradient-to-br from-black via-gray-900 to-[#1e1b4b] p-4 text-white">
      <h2 className="text-xl font-bold mb-4">API Status</h2>
      {health ? (
        <div className="mb-4">
          <p>Status: <span className={health.status === 'healthy' ? 'text-green-400' : 'text-red-400'}>{health.status}</span></p>
        </div>
      ) : (
        <p>Loading health...</p>
      )}

      <h2 className="text-xl font-bold mb-4">Cache Stats</h2>
      {cacheStats ? (
        <div>
          <p>Total Cached Files: {cacheStats.total_cached_files}</p>
          <p>Total Cache Size: {cacheStats.total_cache_size_mb} MB</p>
        </div>
      ) : (
        <p>Loading cache stats...</p>
      )}

      <h2 className="text-xl font-bold mt-8 mb-4">Supported File Types</h2>
      <ul>
        <li>PDF</li>
        <li>Excel (XLS, XLSX)</li>
        <li>PowerPoint (PPT, PPTX)</li>
        <li>Word (DOC, DOCX)</li>
        <li>Images (JPG, PNG, etc.)</li>
        <li>ZIP Archives</li>
      </ul>
    </div>
  );
};

export default Sidebar;
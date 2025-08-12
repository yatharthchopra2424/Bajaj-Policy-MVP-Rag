import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const ResponseChart = () => {
  const data = {
    labels: ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s'],
    datasets: [
      {
        label: 'Response Time',
        data: [12, 19, 3, 5, 2, 3, 7, 8],
        fill: false,
        backgroundColor: 'rgb(75, 192, 192)',
        borderColor: 'rgba(75, 192, 192, 0.2)',
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Response Data by Response Time',
      },
    },
  };

  return <Line data={data} options={options} />;
};

export default ResponseChart;
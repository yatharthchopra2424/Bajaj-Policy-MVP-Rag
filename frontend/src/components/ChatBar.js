import React, { useState } from 'react';
import axios from 'axios';

const ChatBar = () => {
  const [url, setUrl] = useState('');
  const [question, setQuestion] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!url || !question) {
      setError('Please provide a URL and a question.');
      return;
    }

    setLoading(true);
    setError('');
    const newHistory = [...history, { type: 'user', message: question }];
    setHistory(newHistory);

    try {
      const response = await axios.post('http://localhost:8000/hackrx/run', {
        documents: url,
        questions: [question],
      });
      const answer = response.data.answers[0];
      setHistory([...newHistory, { type: 'bot', message: answer }]);
    } catch (err) {
      const errorMessage = err.response ? err.response.data.error : 'An unexpected error occurred.';
      setError(errorMessage);
      setHistory([...newHistory, { type: 'bot', message: `Error: ${errorMessage}` }]);
    } finally {
      setLoading(false);
      setQuestion('');
    }
  };

  return (
    <div className="bg-gray-200 p-4">
      <div className="container mx-auto">
        <div className="flex-grow overflow-y-auto p-4 bg-white rounded-lg shadow-inner mb-4 h-64">
          {history.map((item, index) => (
            <div key={index} className={`flex ${item.type === 'user' ? 'justify-end' : 'justify-start'} mb-2`}>
              <div className={`p-2 rounded-lg ${item.type === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}>
                {item.message}
              </div>
            </div>
          ))}
          {loading && <div className="text-center">Loading...</div>}
          {error && <div className="text-red-500 text-center">{error}</div>}
        </div>
        <form onSubmit={handleSubmit} className="flex flex-col md:flex-row items-center space-y-4 md:space-y-0 md:space-x-4">
          <input
            type="text"
            placeholder="Document URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="p-2 border rounded-lg w-full md:w-1/3"
          />
          <input
            type="text"
            placeholder="Ask a question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            className="p-2 border rounded-lg w-full md:flex-grow"
          />
          <button type="submit" className="bg-blue-500 text-white p-2 rounded-lg w-full md:w-auto" disabled={loading}>
            {loading ? 'Sending...' : 'Send'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatBar;
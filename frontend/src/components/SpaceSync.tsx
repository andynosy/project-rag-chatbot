import React, { useState } from 'react';
import axios from 'axios';

export const SpaceSync: React.FC = () => {
  const [spaceKey, setSpaceKey] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleSync = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!spaceKey.trim()) return;

    setIsLoading(true);
    setMessage('');

    try {
      const response = await axios.post(
        `${import.meta.env.VITE_API_URL}/api/confluence/sync/${spaceKey}`
      );
      setMessage(response.data.message);
      setSpaceKey('');
    } catch (error) {
      setMessage('Error syncing space. Please try again.');
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="border rounded-lg p-4 bg-gray-50">
      <h2 className="text-lg font-semibold mb-2">Sync Confluence Space</h2>
      <form onSubmit={handleSync} className="flex gap-2">
        <input
          type="text"
          value={spaceKey}
          onChange={(e) => setSpaceKey(e.target.value)}
          placeholder="Enter Space Key"
          className="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={isLoading || !spaceKey.trim()}
          className="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 disabled:bg-gray-400"
        >
          {isLoading ? 'Syncing...' : 'Sync'}
        </button>
      </form>
      {message && (
        <p className={`mt-2 text-sm ${
          message.includes('Error') ? 'text-red-600' : 'text-green-600'
        }`}>
          {message}
        </p>
      )}
    </div>
  );
}
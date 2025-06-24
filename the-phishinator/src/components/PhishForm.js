import React, { useState } from 'react';

const PhishForm = ({ onAnalyze, isLoading }) => {
  const [url, setUrl] = useState('');

  const normalizeUrl = (input) => {
    // If input doesn't start with http:// or https://, prepend http://
    if (!/^https?:\/\//i.test(input.trim())) {
      return 'http://' + input.trim();
    }
    return input.trim();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (url.trim()) {
      const normalizedUrl = normalizeUrl(url);
      onAnalyze(normalizedUrl);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="phish-form">
      <input
        type="text" // changed from "url" to "text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="example.com or https://example.com"
        className="url-input"
        required
        disabled={isLoading}
      />
      <button
        type="submit"
        className={`analyze-button ${isLoading ? 'loading' : ''}`}
        disabled={isLoading}
      >
        {isLoading ? (
          <>
            <span className="spinner"></span> ANALYZING...
          </>
        ) : (
          "ANALYZE URL"
        )}
      </button>
    </form>
  );
};

export default PhishForm;

import React from 'react';

const ResultsDisplay = ({ results, isLoading }) => {
  if (isLoading) {
    return (
      <div className="results-loading">
        <div className="spinner"></div>
        <p>Scanning for phishing indicators...</p>
      </div>
    );
  }

  if (!results) return null;

  if (results.error) {
    return (
      <div className="results-error">
        <h3>⚠️ Error</h3>
        <p>{results.error}</p>
        <p className="details">{results.details}</p>
      </div>
    );
  }

  return (
    <div className={`results-container ${results.isPhishing ? 'phishing' : 'safe'}`}>
      <h2>Scan Results</h2>
      <p><strong>URL:</strong> <a href={results.url} target="_blank" rel="noopener noreferrer">{results.url}</a></p>
      <p><strong>Status:</strong> <span className="status">
        {results.isPhishing ? '⚠️ PHISHING DETECTED' : '✅ SAFE'}
      </span></p>
      <p><strong>Confidence:</strong> {(results.confidence * 100).toFixed(2)}%</p>
      <p><strong>Details:</strong> {results.details}</p>
      <p className="timestamp"><em>Scanned at: {new Date(results.timestamp).toLocaleString()}</em></p>
    </div>
  );
};

export default ResultsDisplay;

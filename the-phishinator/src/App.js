import React, { useState } from 'react';
import './App.css';
import PhishForm from './components/PhishForm';
import ResultsDisplay from './components/ResultsDisplay';
import { API_CONFIG } from './config';

function App() {
  const [results, setResults] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleAnalysis = async (url) => {
    setIsLoading(true);
    try {
      const response = await fetch(`${API_CONFIG.BASE_URL}${API_CONFIG.ENDPOINTS.PREDICT}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) throw new Error(`Backend error: ${response.status}`);

      const data = await response.json();
      
      // Transform backend response for frontend display
      setResults({
        url: data.url,
        isPhishing: data.is_phishing,
        confidence: data.confidence,
        details: data.details || "No additional details available.",
        timestamp: data.timestamp
      });

    } catch (error) {
      setResults({ 
        error: error.message,
        details: "Ensure the backend is running on port 5000."
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="content">
        <h1 className="title"><span className="phishinator-text">THE PHISHINATOR</span></h1>
        <p className="dare-text">Click if you dare. I'll be waiting.</p>
        <PhishForm onAnalyze={handleAnalysis} isLoading={isLoading} />
        <ResultsDisplay results={results} isLoading={isLoading} />
      </div>
    </div>
  );
}

export default App;
// API Configuration
export const API_CONFIG = {
  BASE_URL: process.env.NODE_ENV === 'development' 
    ? 'http://localhost:5000' 
    : 'https://your-production-api.com',
  ENDPOINTS: {
    PREDICT: '/predict'
  }
};
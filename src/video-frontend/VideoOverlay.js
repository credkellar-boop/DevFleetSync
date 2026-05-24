// src/video-frontend/VideoOverlay.js
export const VideoOverlay = () => (
  <div className="branding-container">
    <div className="logomark-bullish" /> {/* Your custom branding */}
    <WebRTCClient />
    <div className="status-badge-green">LIVE</div> {/* The "Green Check" status */}
  </div>
);

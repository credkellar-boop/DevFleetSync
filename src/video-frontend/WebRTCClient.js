import React, { useEffect, useRef } from 'react';

const WebRTCClient = ({ roomId, token }) => {
  const localVideoRef = useRef(null);
  const peerConnection = useRef(new RTCPeerConnection({
    iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
  }));

  useEffect(() => {
    // 1. Initialize Camera
    navigator.mediaDevices.getUserMedia({ video: true, audio: true })
      .then(stream => {
        localVideoRef.current.srcObject = stream;
        stream.getTracks().forEach(track => peerConnection.current.addTrack(track, stream));
      });

    // 2. Connect to Signaling Server
    const ws = new WebSocket(`wss://your-domain.com/ws?id=${roomId}`);
    ws.onmessage = async (message) => {
      const data = JSON.parse(message.data);
      if (data.offer) {
        await peerConnection.current.setRemoteDescription(new RTCSessionDescription(data.offer));
        const answer = await peerConnection.current.createAnswer();
        await peerConnection.current.setLocalDescription(answer);
        ws.send(JSON.stringify({ answer }));
      }
    };
  }, [roomId]);

  return <video ref={localVideoRef} autoPlay playsInline muted />;
};

export default WebRTCClient;

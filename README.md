# Video-Gateway: Real-Time Engagement Engine

[![Build Status](https://github.com/darionkellar/video-gateway/actions/workflows/deploy-gateway.yml/badge.svg)](https://github.com/darionkellar/video-gateway/actions)
[![Security Audit](https://img.shields.io/badge/security-validated-green.svg)](https://github.com/darionkellar/video-gateway/security)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Reputation-Gated](https://img.shields.io/badge/Access-Deployma-purple.svg)](https://deployma.io)

## Overview
**Video-Gateway** is a high-performance WebRTC signaling server and engagement module designed for the *DevFleetSync* ecosystem. It bridges the gap between real-time video conferencing and your automated infrastructure, providing secure, reputation-gated access to video streams.

## Core Features
*   **Signaling Engine:** Lightweight Go implementation for P2P WebRTC handshakes.
*   **Security:** Integrated with `src/auth` for JWT-based session validation.
*   **Analytics:** Automated JSON session logging for repository reporting.
*   **Infrastructure:** Fully containerized via `deployma` for seamless integration.

## Reputation & Access
This module utilizes your **Deployma** credentials. Access is restricted based on reputational credit:
*   **Required Credit Score:** >500
*   **Authentication:** Must provide valid bearer token through the websocket header.

## System Health
| Service | Status | Last Audit |
| :--- | :--- | :--- |
| `video-gateway` | ✅ Active | 2026-05-23 |
| `go_watchdog` | ✅ Monitoring | 2026-05-23 |
| `session-logger`| ✅ Logging | 2026-05-23 |

## Integration
This module is designed to work in tandem with the *Master-Trading-Fleet* engine. All session metadata is pushed to the `./logs/video_sessions.log` directory for real-time repository health tracking.

---
*Maintained by the DevFleetSync Infrastructure Team.*

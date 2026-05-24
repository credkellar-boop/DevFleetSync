package main

import (
	"encoding/json"
	"os"
	"time"
)

type SessionEntry struct {
	ClientID  string    `json:"client_id"`
	StartTime time.Time `json:"start_time"`
	EndTime   time.Time `json:"end_time"`
	Duration  float64   `json:"duration_minutes"`
}

func LogSession(clientID string, start time.Time, end time.Time) {
	entry := SessionEntry{
		ClientID:  clientID,
		StartTime: start,
		EndTime:   end,
		Duration:  end.Sub(start).Minutes(),
	}

	file, _ := os.OpenFile("./logs/video_sessions.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	defer file.Close()
	
	json.NewEncoder(file).Encode(entry)
}

package main

import (
	"fmt"
	"net/http"
	"time"
)

func monitorGateway(url string) {
	for {
		resp, err := http.Get(url + "/_/health") // Custom health endpoint
		if err != nil || resp.StatusCode != 200 {
			fmt.Printf("Alert: Video Gateway unstable at %s\n", time.Now().Format(time.RFC3339))
			// Trigger your notification bridge here (e.g., send to Slack/Discord)
		}
		time.Sleep(30 * time.Second)
	}
}

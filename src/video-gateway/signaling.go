package main

import (
	"log"
	"net/http"
	"sync"
	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{CheckOrigin: func(r *http.Request) bool { return true }}
var clients = make(map[string]*websocket.Conn)
var mu sync.Mutex

func handleConnections(w http.ResponseWriter, r *http.Request) {
	ws, _ := upgrader.Upgrade(w, r, nil)
	defer ws.Close()

	// Simple ID registration logic
	clientID := r.URL.Query().Get("id")
	mu.Lock()
	clients[clientID] = ws
	mu.Unlock()

	for {
		var msg map[string]interface{}
		err := ws.ReadJSON(&msg)
		if err != nil {
			break
		}
		// Relay message to target peer
		target := msg["target"].(string)
		mu.Lock()
		if targetConn, ok := clients[target]; ok {
			targetConn.WriteJSON(msg)
		}
		mu.Unlock()
	}
}

func main() {
	http.HandleFunc("/ws", handleConnections)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

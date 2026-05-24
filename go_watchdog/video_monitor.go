func VerifyLogs() {
    // Check if the log file is being updated
    info, err := os.Stat("./logs/video_sessions.log")
    if err == nil && time.Since(info.ModTime()).Minutes() < 60 {
        fmt.Println("[STATUS] Video session logging active - Green Check Verified")
    } else {
        fmt.Println("[ALERT] Log inactivity detected - Review required")
    }
}

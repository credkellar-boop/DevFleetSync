# Use official Go image
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o video-gateway .

# Final stage
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/video-gateway .
# Ensure log directory exists
RUN mkdir -p /root/logs
EXPOSE 8080
CMD ["./video-gateway"]

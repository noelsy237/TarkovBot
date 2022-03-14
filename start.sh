if docker inspect --format="{{.State.Running}}" tarkov-bot; then
    echo "Container is running"
    docker stop tarkov-bot
    docker rm tarkov-bot
else
    echo "Container is not running"
fi
docker build -t tarkov-bot .
docker run -d --name=tarkov-bot --restart unless-stopped tarkov-bot
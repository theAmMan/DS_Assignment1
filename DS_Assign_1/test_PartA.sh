HOST=127.0.0.1
PORT=8000

curl http://${HOST}:${PORT}/topics/
echo -e "\n"
curl -XPOST "http://${HOST}:${PORT}/topics/" -d topic_name=Kagenou
echo -e "\n"
curl -XPOST "http://${HOST}:${PORT}/topics/" -d topic_name=Kagenou
echo -e "\n"
curl -XPOST "http://${HOST}:${PORT}/topics/" -d topic_name=Minoru
echo -e "\n"
curl http://${HOST}:${PORT}/topics/
echo -e "\n"
curl -XPOST "http://${HOST}:${PORT}/producer/register" -d topic_name=Minoru
echo -e "\n"
curl -XPOST "http://${HOST}:${PORT}/consumer/register" -d topic_name=Minoru
echo -e "\n"

# sleep 5m
## Remote launch

Документация по гриду: https://www.selenium.dev/documentation/en/grid/

### Some config lines

For Edge:

```bash
java "-Dwebdriver.edge.driver=c:\bin\msedgedriver.exe" -jar .\selenium-server-standalone-3.141.59.jar -role node -nodeConfig .\nodeWindows.json
>>> pytest --browser MicrosoftEdge
```

For Yandex:

```bash
java "-Dwebdriver.chrome.driver=c:\bin\yandexdriver.exe" -jar .\selenium-server-standalone-3.141.59.jar -role node -nodeConfig .\nodeWindows.json
>>> pytest --browser chrome
```

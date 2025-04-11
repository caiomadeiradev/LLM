# LLM
Testing LLM models and applications.

### Postgres SQL Database (alternative installation):

In case of:
```
>> sudo apt install postgresql-16

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package postgresql-16
 ```

Try:
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

udo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

sudo apt update

sudo apt install postgresql-16
```
### PGVector vectorial database
In case of:
```
>>make
gcc -Wall -Wmissing-prototypes -Wpointer-arith -Wdeclaration-after-statement -Werror=vla -Wendif-labels -Wmissing-format-attribute -Wimplicit-fallthrough=3 -Wcast-function-type -Wshadow=compatible-local -Wformat-security -fno-strict-aliasing -fwrapv -fexcess-precision=standard -Wno-format-truncation -Wno-stringop-truncation -g -g -O2 -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fno-omit-frame-pointer -march=native -ftree-vectorize -fassociative-math -fno-signed-zeros -fno-trapping-math -fPIC -fvisibility=hidden -I. -I./ -I/usr/include/postgresql/16/server -I/usr/include/postgresql/internal  -Wdate-time -D_FORTIFY_SOURCE=2 -D_GNU_SOURCE -I/usr/include/libxml2   -c -o src/bitutils.o src/bitutils.c
src/bitutils.c:1:10: fatal error: postgres.h: No such file or directory
    1 | #include "postgres.h"
      |          ^~~~~~~~~~~~
compilation terminated.
make: *** [<builtin>: src/bitutils.o] Error 1
```

Try:
```
sudo apt install postgresql-server-dev-16
```

### Docker compose up
In case of:
```
caiomadeira@caiomadeira-G3-3500:~/Desktop/langfuse$ sudo docker compose up
[sudo] password for caiomadeira: 
[+] Running 6/6
 ✔ Container langfuse-redis-1            Running                                         0.0s 
 ✔ Container langfuse-postgres-1         Created                                         0.0s 
 ✔ Container langfuse-clickhouse-1       Running                                         0.0s 
 ✔ Container langfuse-minio-1            Running                                         0.0s 
 ✔ Container langfuse-langfuse-web-1     Running                                         0.0s 
 ✔ Container langfuse-langfuse-worker-1  Runni...                                        0.0s 
Attaching to clickhouse-1, langfuse-web-1, langfuse-worker-1, minio-1, postgres-1, redis-1
Gracefully stopping... (press Ctrl+C again to force)
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint langfuse-postgres-1 (302e863df72631a724cc57537d74db43a877b71a2f747c4d65b498855b8db5cb): failed to bind host port for 127.0.0.1:5432:172.18.0.7:5432/tcp: address already in use

```

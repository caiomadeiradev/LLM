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
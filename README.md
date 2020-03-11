# View locally

1. clone repository (if you are not me, then **fork** it)

```bash
git clone https://github.com/sharepointoscar/presentations.git

2. run within Docker locally.

```
```bash
docker run -it -v {WORKINGDIR}:/repo -p 9000:9000 gitpitch/desktop:pro
```
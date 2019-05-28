Source: http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/
PyQt4: https://iqbalnaved.wordpress.com/2014/05/31/installing-pyqt4-for-python-2-7-6-in-virtual-environement-in-ubuntu-14-04/

Build command:
```
docker build -t m4baker-gui .
```

Run command:
```
docker run -ti --rm \
       -e DISPLAY=$DISPLAY \
       -v /tmp/.X11-unix:/tmp/.X11-unix \
       -v /home/mshepelev/Documents:/home/mshepelev/Documents \
       m4baker-gui
``` 
 

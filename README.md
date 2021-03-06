### Data Enhancement

`train/MRI/AD` for example

- adaptive roi crop 
- resize to 256x256 and fill background with black
- remove salt and pepper noise with median filtering
- randomly rotate / filp / brightness / contrast

<img src=https://gitee.com/tiiaan/repo/raw/master/img/202109092207217.png width=150/><img src=https://gitee.com/tiiaan/repo/raw/master/img/202109092208607.png width=150/><img src=https://gitee.com/tiiaan/repo/raw/master/img/202109092209160.png width=150/>

<img src=https://gitee.com/tiiaan/repo/raw/master/img/202109092208904.png width=150/><img src=https://gitee.com/tiiaan/repo/raw/master/img/202109092208741.png width=150/><img src=https://gitee.com/tiiaan/repo/raw/master/img/202109092209113.png width=150/>

&nbsp;

### Train

train MRI and PET data together based on `ResNet50` to predict AD/NC on the test set.

&nbsp;

### How to Run

```shell
git clone https://github.com/tiiaan/alzheimer
cd /alzheimer
pip install -r requirements.txt
python train.py
```

you could download the final data set from google drive [`HERE`]().


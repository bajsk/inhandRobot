# Inhand HSR Robot Object Saliency Segmentation #
***

## Train Data ##
- Train data include 3 following categories
```text
background
robot_hand
inhand_object
```

- Segmentation Color Chart

![Color Chart](./docs/images/legend.png)

- Data Samples

| ![Sample1](./docs/images/sample1.png "sample-1") | ![Sample2](./docs/images/sample2.png "sample-2") |
|:---:|:---:|
| ![Sample3](./docs/images/sample3.png "sample-3") | ![Sample4](./docs/images/sample4.png "sample-4") |

## Test code ##
***
 - `python scripts/test_image_inhand.py`
 - Sample result
   <p align="center">
    <img src="docs/images/inhand.png", width="480">
   </p>
   <p align="center">
    <img src="docs/images/prediction.png", width="480">
   </p>

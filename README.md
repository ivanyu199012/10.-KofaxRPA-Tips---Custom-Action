# Examples of custom action
Example code are organized as below:
- `NodeJs` folder = custom action (Node.js) example code
- `Python` folder = custom action (Python) example code

## Blog post

## Custom Action (Node.js)

### Requirements
- Node.js 12.22.1

### Setup
```cmd
git clone https://github.com/ivanyu199012/10.-KofaxRPA-Tips---Custom-Action
cd 10.-KofaxRPA-Tips---Custom-Action\NodeJs\node_modules\sampleHandler

npm install
cd ../../

node test.js
```

If everything is fine, you should see an output as below:
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1667889039060/_BIVizCVF.png)


## Custom Action (Python)
### Requirements
- Python 3.9.10
- Virtualenv 20.13.1 (optional)

### Setup
```
git clone https://github.com/ivanyu199012/10.-KofaxRPA-Tips---Custom-Action
cd 10.-KofaxRPA-Tips---Custom-Action\Python

virtualenv customActionEnv
customActionEnv\Scripts\activate

pip install -r requirements.txt
python testSampleHandler.py
```

If everything is fine, you should see an output as below:
![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1667975847582/grBWkbFT0.png)
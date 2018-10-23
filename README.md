# Non-barcoded item recognition for self-checkout and regular Point-of-sale

## Problem definition
- Retailers sell up to 300 non-barcoded items
- At self-checkout customers are presented with up to 6-layers tree to pick the correct item
- Cashiers at regular Point-of-Sales are trained to remember codes or look through a book to identify the item

## Proposed solution
- Install a camera to take a photo of the item placed on a self-checkout or in POS
- Train a Neural Network 
- Use computer vision and trained NN to recognize the item
- Present the customer/cashier with reduced number of items
![alt text](Visuals/Concept.jpg "")

## Dataset
- Image-net (and Google)
- 20 classes (fruits)
- 16K+ sample images
- 90% training, 10% for validation
![alt text](Visuals/Classes_And_Counts.jpg "")

## Techniques used
- Deep learning
- Keras with Tensorflow backend
- Very simple Convolutional Neural Network

## Results received
- 38.2% top-1 and 80.4% top-5 accuracy (on validation set). 
- That means 80.4% of the times correct label would be in list of reduced items if 5 are shown (as in pseudo-screen above)

## Samples: 
- 5 top predictions with probabilities presented
- Green - true label (all 5 orange indicate correct label not among to 5 guesses)
- True label at the bottom of each legend
![alt text](Visuals/top5_1.jpg "")
[More...](TopPredictions.md)


## Intermediate layers: 
- As each neuron activates on a rather small patch of an image
- I pick a random neuron from some layer
- For the given neuron, I loop through the data set to get the images which activate the given neuron the most
- And display these image patches

How to understand the images bellow:
- Each picture contains representations of 9 different neurons (3x3 big squares)
- Each neuron square contains 16 (4x4) image patches which activated that neuron the most
- Example:
  - Image bellow represents 9 convolutional layer 3 neurons
  - Top-left neuron has 16 images which look like a shark
  - Middle-left neuron recongized a blue bird
  - Middle-middle neuron has a few different classes in it

![alt text](Visuals/V40/L3/interim_19.jpg "")

Check more images of intermediate convolutional layers [L1](L1_intermediate.md), [L2](L2_intermediate.md), [L3](L3_intermediate.md), [L4](L4_intermediate.md), [L5](L5_intermediate.md).
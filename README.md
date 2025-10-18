
# US CURRENCY DETECTION

This project is designed to detect the denomination and quantity of U.S. CASH currency in an image. It supports PNG, JPG, and JPEG file formats.



Please do not upload any sensitive or malicious files.
## Installation

This product was deployed via Onrender so just access this link: 
https://us-currency-detection.onrender.com

Disclaimer: After accessing link you must wait a bit for site to boot up. This is because I have a free plan with Onrender.

## Q&A

#### How was this created?

Using Roboflow, a platform that simplifies the entire computer vision workflow, I created a dataset consisting of over 1000 images. Afterwards I trained the model and made it accessible to online here: https://app.roboflow.com/clashbot-artum/dollar-classify-vq2yo/visualize/2

#### How accurate is this model?

My model has a mAP@50 of 94.0% Where mAP@50 is equal to the mean of the Average Precision metric across all classes in a model at a 50% IoU threshold. And has a precision of 90.7%. Which measures how often a model's predictions are correct. Lastly, it has a recall of 88.0%. Where recall measures what percentage of relevant labels were successfully identified. 

## License

[MIT](https://choosealicense.com/licenses/mit/)


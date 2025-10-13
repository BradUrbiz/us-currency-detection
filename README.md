
# US CURRENCY DETECTION

This project is designed to detect the denomination and quantity of U.S. CASH currency in an image. It supports PNG, JPG, and JPEG file formats.



Please do not upload any sensitive or malicious files.
## Installation

This product was deployed via Onrender so just access this link: 
https://us-currency-detection.onrender.com

Disclaimer: After accessing link you must wait a bit for site to boot up. This is because I have a free plan with Onrender.

## FAQ

#### How was this created?

Using Roboflow, a platform that simplifies the entire computer vision workflow, I created a dataset consisting of over 1000 images. Afterwards I trained the model and made it accessible to online here: https://app.roboflow.com/clashbot-artum/dollar-classify-vq2yo/visualize/2

Once model was complete, I utilized HTML to create a simple frontend. It consisted just of a page that outlined my project and allowed for file uploads. For the backend I used Flask to temporarily save the image and send it my own Roboflow model. Lastly, I pushed this all to github and deployed it with Onrender to get my finished product.

#### How accurate is this model?
My model has a mAP@50 of 94.0% Where mAP@50 is equal to the mean of the Average Precision metric across all classes in a model at a 50% IoU threshold. And has a precision of 90.7%. Which measures how often a model's predictions are correct. Lastly, it has a recall of 88.0%. Where recall measures what percentage of relevant labels were successfully identified. 

#### For the Youth Coders Hack 2025, how does this relate to the topic of "Social Good"?

This project contributes to Social Good by making currency recognition more accessible and efficient. By allowing users to upload an image and instantly identify both the denomination and quantity of U.S. currency, the tool can support individuals with visual impairments, cash handling challenges, or language barriers.

It can be used by educational programs, nonprofits, or financial literacy initiatives to help people better understand and manage physical money. The website is fully online, easy to use, and integrates Roboflow for accurate predictions.

By simplifying currency identification, this project promotes financial accessibility, inclusion, and independence—all of which align with the core goals of social good.

## Creation

Created as an entry in Youth Coders Hack 2025


## License

[MIT](https://choosealicense.com/licenses/mit/)


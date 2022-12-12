### Problem statement
A developer has contracted me to determine which building decisions are the most impactful to the value of a property.  I will examine the Ames housing data to identify factors of development that should be kept in mind as the developer seeks to effectively allocate capital and planning recourses.

### Methodology
I began with investigating the [dataset](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).
This dataset provides the data dictionary and general information.

I then examined key distributions and correlations, with a focus on determing relationships with the target variable of sale price.
I also looked for evidence of multi-collinearity among variables most correlated with sale price.

The evidence of multicollinearity, which is to be expected to some degree as the high mutual correlations with saleprice indicate a shared relationship, lead me to the hypothesis that regularization of the parameters could lead to stronger inferences about the features predictive of sale price.

### EDA
I discovered that the log of the saleprice is much closer to normally distributed with no noticeable skew.  There are a few outliers on the left, which is not particularly concerning and to be expected since the price of a small teardown lot would understandably be significantly lower than the typical home.

The distribution here indicates that normally distributed residuals would more likely result from modeling with the log of saleprice as the response.  The predicted value could then be exponentiated to arrive at the dollar estimate of price as opposed to the log-dollar estimate.

In the current analysis I stick with the untransformed saleprice as the response.

Not surprisingly, there is substantial multicollinearity between the ten variables that are most correlated with saleprice.  This suggests that regularization in the modeling phase will be very important so as to remove excess features that are collinear with other features.  

For instance, year built, year remodel add, and garage year built are all related (you can't remodel before the building is built).

There an almost quadratic relationship between overall quality and mean sale price.  

I would have expected the houses in the best condition to have the highest price per square foot of above ground living area. This does not appear to be the case, which leads me to believe that the impact of overall condition on saleprice is confounded by the above ground living area.
### Data cleaning

There don't seem to be many pools in Ames (9). Likewise, only 65 houses have Miscelaneous Features (3.17%), so I believe it is reasonable to drop this feature. Also, there are 1911 out of 2051 houses without an alley. I'm going to remove this feature. There are a significant number of fences (400), so I'll impute "None" for the NA values. It would be difficult to draw conclusions from columns 'Pool QC' and 'Pool Area', as there are only 9 houses with pools.

Likewise for Misc Feature, Alley, and Fence, these do not strike me as frequent enough and/or important enough to include as a predictive feature. I will drop all four columns.

I dropped PID because this feature is reduntant with ID for data identification purposes. ID I will keep for maintining identification of the data.

I changed the 'ms_subclass' feature to categorical.

### Feature Identification
I used the gini index, the standard deviation of the the sale price according to category, and finally the multiple of the two values to arrive at the features with the most variation in sale price, adjusted for the gini (an information metric indicating the iner-class dispersion for a feature).  exterior_qual, exterior_1st appear to be important with regard to sale price after adjusting for their category dispersion.

### Feature Engineering
From graphical investigation, it is apparent that there is significant variation in the mean sale price for the various exterior materials for given quality levels.  The exterior quality appears to explain more of the variance in the saleprice, but the material also appears to have some explanatory power.  The influence of the material appears to be different for each quality, so I created a feature that is their combination.

### Modeling

For modeling, I first one-hot encoded the data.  I then standard scaled the variables and then attempted regression with unregularized linear regression followed by the lasso, ridge regression, and elastic net regression.

The best model as determined by the R-squared statistic and the RMSE was the elastic net with an l1 ratio of .99.  This generated the best validation set scores, though there is still evidence of overfitting due to the difference between the training and the validation set scores.

Elastic Net provided the best validation set performance.

### Conclusions

From the  analysis, I found that the exterior quality / material features with the coefficient of the largest magnitude corresponds to ext_qual_1st_ExVinylSd.

Further development should consider vinyl siding for houses with excelent exterior quality.

### Areas for further analysis
I could have preprocessed and selected features more extensively in advance of the modeling phase.  This would have allowed for looking at interaction terms with less danger of overfitting and overstepping computational constraints.  In particular,  interaction terms for garage should have been utilized.  This would have negated the negative impact of imputing 0 for the missing values of garage year.

Different encoding paths for continuous variables.

### Problem statement
A developer has contracted me to determine which building decisions are the most impactful to the value of a property.  I will examine the Ames housing data to identify factors of development that should be kept in mind as the developer seeks to effectively allocate capital and planning recourses.

### Methodology
I began with investigating the [dataset](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).
This dataset provides the data dictionary and general information.

I then examined key distributions and correlations, with a focus on determing relationships with the target variable of sale price.
I also looked for evidence of multi-collinearity among variables most correlated with sale price.

The evidence of multicollinearity, which is to be expected to some degree as the high mutual correlations with saleprice indicate a shared relationship, lead me to the hypothesis that regularization of the parameters could lead to stronger inferences about the features predictive of sale price.

Also, the vast number of features available, even more a



### Areas for further analysis
#### Methodology
I could have preprocessed and selected features more extensively in advance of the modeling phase.  This would have allowed for looking at interaction terms with less danger of overfitting and overstepping computational constraints.  In particular,  interaction terms for garage should have been utilized.  This would have negated the negative impact of imputing 0 for the missing values of garage year.

Different encoding paths for continuous variables.

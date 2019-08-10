# Fitbit-Sleep

Hi everyone! Here's a little Fitbit API I built in python to grab Sleep Stages. It's adapted from: https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873, which is well worth the read if you're new to the Fitbit API or to using data science for Quantified Self research. My main adaptation was to update the Fitbit API version call from 1.0 to 1.2 -- which is the only version that returns actual Sleep Stages (Deep, Light, Wake, REM). I also indexed a pandas dataframe for the returned results. 

For the code to work for you, you'll need to update lines 12 & 13 with your CLIENT ID & CLIENT SECRET, which you get from dev.fitbit.com. If you want to save your outputs, make sure YOUR_PATH is updated in line 59.

That's it! Enjoy!



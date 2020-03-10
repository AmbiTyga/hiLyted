# Video_Highlighter
Sports entertainment is a type of spectacle which presents an ostensibly competitive event using a high level of theatrical flourish and extravagant presentation, with the purpose of entertaining an audience.It maintains or improves physical ability and skills while providing enjoyment to participants and entertainment for spectators.Hence a sports highlight is needed as it provides a spectator important information for planning and researching on strategies. It provides the spectator to analyze so that he could perform better in his own game. A sports highlight video are clips of the game footage that highlight individual's talent and skills.They have the most positive and impactful effects on the individuals involved.<br>Piecing together a highlight reel of the season isn’t that difficult anymore. There are plenty of amateur video buffs out there with a camcorder and some editing software who know how to edit highlights to a music track. But producing a season ending film that captures not only highlights but the heart and spirit of a team is much more difficult.<br> This project deals with this difficulty by providing a great method in making a video highlight.The project is based on speech analysis. There are various audios which can be used as the dataset for analysing. This project deals with the audio to extract important features from it and provide us with important part of the video from a sports video.

## Setup Instructions
After cloning or downloading run following command in the console:<br>

	$ package.sh
	$ python main.py

(Note: For a long video length use colab/sagemaker. Provided `main.ipynb` for colab/sagemaker.)
## Methodology:
 My method is based on simple speech analysis and short time energy of the sound.
 ### What is short time energy?
 An audio signal can be analyzed in the time or frequency domain. In the time domain, an audio signal is analyzed with respect to the time component, whereas in the frequency domain, it is analyzed with respect to the frequency component:

![automatic highlight generation](Documents\image.jpg)

The energy or power of an audio signal refers to the loudness of the sound. It is computed by the sum of the square of the amplitude of an audio signal in the time domain. When energy is computed for a chunk of an entire audio signal, then it is known as Short Time Energy.
### Steps:
- Download audio and video from video's link.
- Extract audio's feature: Audio data and sampling rate.
- Find short time energy.
- Determine a better short time energy.
- Store start and end time of high energy clip.
- Replace consecutive clips with a single clip.
- Extract the clip and store in the destination folder

## Refrences
- [Librosa-Python package for audio analysis](https://librosa.github.io/librosa/)
- [Youtube-dl-For downloading videos](https://github.com/ytdl-org/youtube-dl)
- [Simple Speech Analysis](https://towardsdatascience.com/beginners-guide-to-speech-analysis-4690ca7a7c05)
- [Short time energy](Documents\Short_time_energy.pdf)


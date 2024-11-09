
import pyaudio
import wave

def play_sound(file_path):
    chunk = 1024

    # Open the audio file
    wf = wave.open(file_path, 'rb')

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream to play the audio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),   

                    output=True)

    # Read   
 and play chunks of audio data
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    # Close the stream and PyAudio object
    stream.stop_stream()
    stream.close()
    p.terminate()

# Example usage:
play_sound("my_music.wav")
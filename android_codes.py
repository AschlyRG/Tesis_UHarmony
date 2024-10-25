from jnius import autoclass,cast
from android.runnable import run_on_ui_thread
MediaPlayer = autoclass('android.media.MediaPlayer')
PythonActivity = autoclass("org.kivy.android.PythonActivity")
AndroidString = autoclass('java.lang.String')
Toast = autoclass('android.widget.Toast')

@run_on_ui_thread
def show_toast(text='Hello'):
    context = PythonActivity.mActivity
    text_char_sequence = cast('java.lang.CharSequence', AndroidString(text))
    duration = Toast.LENGTH_SHORT
    toast = Toast.makeText(context, text_char_sequence, duration)
    toast.show()


def play_media(file_path):
    _player = MediaPlayer()
    _player.setDataSource(file_path)
    _player.prepare()
    _player.start()
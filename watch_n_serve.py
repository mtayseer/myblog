import os
from bottle import route, run, static_file
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def watch_n_serve():

    OUTPUT_ROOT = './output'

    @route('/')
    @route('/<path:path>')
    def serve(path='index.html'):
        response = static_file(path, root=OUTPUT_ROOT)

        # if the user wants a directory, I search for index pages
        if path.endswith('/') and response.status_code == 404:
            for file in ['index.html', 'index.htm']:
                response = static_file(path + file, root=OUTPUT_ROOT)
                if response.status_code != 404:
                    return response
        return response

    class BuildEventHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            # Because main.css is generated, I don't want to get into an infinite loop of generation
            generated_css = os.path.abspath(os.path.join(os.path.dirname(__file__), 'theme/littlebigdetails/static/css/main.css'))
            if event.src_path == generated_css:
                return
            super(BuildEventHandler, self).on_moved(event)
            os.system('fab rebuild')

    event_handler = BuildEventHandler()
    content_observer, theme_observer = Observer(), Observer()
    content_observer.schedule(event_handler, './content', recursive=True)
    theme_observer.schedule(event_handler, './theme', recursive=True)
    content_observer.start()
    theme_observer.start()
    try:
        run(host='localhost', port=8080, debug=True)
    finally:
        content_observer.stop()
        content_observer.join()
        theme_observer.stop()
        theme_observer.join()

watch_n_serve()
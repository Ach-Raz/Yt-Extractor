import os
import sys
import urllib.request 

def download_youtube_thumbnail(url: str):
    """
    Estrae l'ID del video da un URL di YouTube e scarica il thumbnail
    direttamente dall'API di immagini di YouTube usando urllib.request.
    """
    print("----------------------------------------------")
    print("🛠️  Inizio download thumbnail (Metodo diretto)...")


    video_id = None
    if "v=" in url:

        video_id = url.split("v=")[-1].split("&")[0]
    elif "embed/" in url:
   
        video_id = url.split("embed/")[-1].split("?")[0]
    else:
        print("\n❌ ERRORE: URL non valido o non riconducibile a un ID video.")
        return


    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"


    filename = f"{video_id}_thumbnail.jpg"
    output_path = os.path.join(os.getcwd(), filename)

    try:

        urllib.request.urlretrieve(thumbnail_url, output_path)

        print("\n✅ Download completato con successo!")
        print("File salvato come:", output_path)

    except Exception as e:
        print(f"\n❌ ERRORE durante il download: {e}")
        print(
            "Suggerimento: Controlla la connettività o se YouTube ha cambiato il formato di immagini."
        )


if __name__ == "__main__":

    if len(sys.argv) > 1:
        youtube_url = sys.argv[1]
    else:

        youtube_url = input("Inserisci l'URL di YouTube: ").strip()

    if youtube_url:
        download_youtube_thumbnail(youtube_url)
    else:
        print("Nessun URL fornito. Script terminato.")

from tqdm import tqdm as tq
import os.path as p
import requests
def DownloadEAFC24(url : str, output_path : str, chunk_size=1024*1024):
    resume_byte_pos = 0
    resume_size = 0
    if(p.exists(output_path)):
        resume_byte_pos = p.getsize(output_path)
    headers = {}
    if resume_byte_pos > 0:
        headers['Range'] = f'bytes={resume_byte_pos}-'
    # Send GET request
    with requests.get(url, stream=True, headers=headers) as response:
        # Check if server supports ranges
        if response.status_code == 416:
            # 416 = Range Not Satisfiable: the file is probably already fully downloaded
            print("Already downloaded.")
            return
        response.raise_for_status()
        # Get total size from header (if provided)
        # If Range used, the content-length might be length of remaining bytes
        total_size_in_resp = response.headers.get('Content-Length')
        if total_size_in_resp is None:
            # no content length header
            total_size = None
        else:
            total_size = int(total_size_in_resp) + resume_byte_pos

        mode = 'ab' if resume_byte_pos else 'wb'

        with open(output_path, mode) as f, tq(
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            initial=resume_byte_pos,
            desc=p.basename(output_path),
            ascii=True,
            miniters=1,
            ncols=80,
        ) as bar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
                    bar.update(len(chunk))
    print("Download complete:", output_path)
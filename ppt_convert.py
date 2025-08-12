import os
import requests
import uuid
import time
import comtypes.client
import pythoncom
from docling.document_converter import DocumentConverter

def download_pptx(url, save_dir="downloads"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_name = f"{uuid.uuid4().hex}.pptx"
    file_path = os.path.join(save_dir, file_name)

    print(f"[INFO] Downloading PPTX from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"[INFO] File downloaded: {file_path}")
        return file_path
    else:
        raise Exception(f"[ERROR] Failed to download file. Status code: {response.status_code}")

def convert_pptx_to_pdf(pptx_path):
    if not pptx_path.lower().endswith((".pptx", ".ppt")):
        raise ValueError("Only .ppt and .pptx files are supported.")

    pptx_path = os.path.abspath(pptx_path)
    pdf_path = os.path.splitext(pptx_path)[0] + ".pdf"

    print(f"[INFO] Converting {pptx_path} to PDF")

    import pythoncom
    try:
        pythoncom.CoInitialize()  # Initialize COM for the current thread
        
        powerpoint = None
        try:
            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            powerpoint.Visible = True  # Keep window visible to avoid automation issues

            deck = powerpoint.Presentations.Open(pptx_path)
            deck.SaveAs(pdf_path, 32)  # 32 = PDF
            deck.Close()
            print(f"[INFO] PDF saved at: {pdf_path}")
            return pdf_path
        except Exception as e:
            print(f"[ERROR] Failed to convert PowerPoint to PDF: {str(e)}")
            raise
        finally:
            if powerpoint:
                try:
                    powerpoint.Quit()
                except:
                    pass
    finally:
        pythoncom.CoUninitialize()  # Clean up COM for the current thread

def convert_pdf_to_markdown(pdf_path):
    print(f"[INFO] Converting PDF to Markdown using Docling")
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    markdown = result.document.export_to_markdown()

    md_path = pdf_path.replace(".pdf", ".md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"[INFO] Markdown saved at: {md_path}")
    return md_path

def convert_powerpoint_to_markdown(file_path, delete_temp_files=True):
    """
    Convert a PowerPoint file to markdown.
    Args:
        file_path: Path to the PowerPoint file (.ppt or .pptx)
        delete_temp_files: Whether to delete temporary PDF file after conversion
    Returns:
        tuple: (markdown_content, error_message)
    """
    pdf_path = None
    try:
        # Convert PowerPoint to PDF
        pdf_path = convert_pptx_to_pdf(file_path)
        if not pdf_path:
            return None, "Failed to convert PowerPoint to PDF"

        # Convert PDF to markdown using docling
        converter = DocumentConverter()
        result = converter.convert(pdf_path)
        markdown_content = result.document.export_to_markdown()

        # Add metadata header
        metadata_header = f"""---
source: {file_path}
type: presentation
converted: {time.strftime('%Y-%m-%d %H:%M:%S')}
---

"""
        markdown_content = metadata_header + markdown_content
        print("[SUCCESS] PowerPoint converted to markdown successfully")
        return markdown_content, None

    except Exception as e:
        error_msg = f"PowerPoint to markdown conversion failed: {str(e)}"
        print(f"[ERROR] {error_msg}")
        return None, error_msg

    finally:
        # Clean up temporary files if requested
        if delete_temp_files and pdf_path and os.path.exists(pdf_path):
            try:
                os.remove(pdf_path)
                print(f"[INFO] Cleaned up temporary PDF: {pdf_path}")
            except Exception as e:
                print(f"[WARNING] Failed to clean up PDF: {e}")

# === Example ===
if __name__ == "__main__":
    pptx_url = "https://hackrx.blob.core.windows.net/assets/Test%20/Test%20Case%20HackRx.pptx?sv=2023-01-03&spr=https&st=2025-08-04T18%3A36%3A56Z&se=2026-08-05T18%3A36%3A00Z&sr=b&sp=r&sig=v3zSJ%2FKW4RhXaNNVTU9KQbX%2Bmo5dDEIzwaBzXCOicJM%3D"
    
    try:
        pptx_file = download_pptx(pptx_url)
        markdown_content, error = convert_powerpoint_to_markdown(pptx_file)
        if error:
            print(f"[ERROR] {error}")
        else:
            print("[SUCCESS] PowerPoint converted to markdown successfully")
    except Exception as e:
        print(f"[ERROR] {str(e)}")
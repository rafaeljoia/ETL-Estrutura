from pipeline.extract import extract_from_excel


if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    print(data_frame_list)
   # data_frame = contact_data_frames(data_frame_list)
   # load_excel(data_frame, "data/output", "output")
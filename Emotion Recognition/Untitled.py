 if gray_scale:
            return self.img_to_landmarks(dlib.load_grayscale_image(img_path), exclude_vector_base)
        return self.img_to_landmarks(dlib.load_rgb_image(img_path), exclude_vector_base)

    def img_to_landmark_points(self, img: np.ndarray) -> List:
        detections = self.detector(img, 1)
        if len(detections) < 1:
            return [None]
        landmark_points_list = []
        for (i, rect) in enumerate(detections):
            shape = self.predictor(img, rect)
            landmark_points_list.append(dt.shape_to_np(shape, size=LAND_MARK_POINTS_SIZE))
        return landmark_points_list

    def img_to_rectangles(self, img: np.ndarray) -> List[Tuple]:
        detections = self.detector(img, 1)
        if len(detections) == 0:
            return [(0, 0, 0, 0)]

        rectangles = []
        for (i, rect) in enumerate(detections):  # loop over the face detections
            # convert dlib's rectangle to a OpenCV-style bounding box, i.e. (x, y, w, h)
            (x, y, w, h) = dt.rectangular_to_bounding_box(rect)

            rectangles.append((x, y, w, h))  # Assumed that number of face in picture = 1
        return rectangles
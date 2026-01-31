or idx,(x, y, r) in enumerate(circles):
            cv.circle(output,(x,y), r, (0, 255,0), 2)
            cv.circle(output,(x,y), 2, (0,0, 255))
            cv.putText(output, f"ID:{idx} r={r}",(x-40, y-r-10), cv.FONT_HERSHEY_PLAIN, 0.5, (255, 0, 0),1)
    combined = np.hstack((image, output))
    plt.figure(figsize=(12, 6))
    plt.imshow(cv.cvtColor(combined, cv.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

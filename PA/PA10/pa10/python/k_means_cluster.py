import collections
def distance(p1, p2):
    # Calculates the Euclidean Distance between two points
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def centroid(points):
    # Computes the centroid of a set of points.
    # The centroid is the "average" point in the set.
    # That is, its x coordinate is the average x among the points in the set
    # and the y coordinate is the average y among the points in the set.
    x = 0
    y = 0
    for i in points:
        x += i[0]
        y += i[1]
    return (x/len(points), y/len(points))

def cluster(reference, points):
    # Clusters the given points using the reference points.
    # Points in the same cluster should be closest to the same reference point.
    # In other words, if points A and B are in cluster i then they should both be
    # closer to reference point i than any of the other reference points.
    cluster_list = [[] for x in range(len(reference))]
    for i in range(0, len(points)):
        closest_distance = float("inf")
        closest_point = 0
        for j in range(0, len(reference)):
            if distance(reference[j], points[i]) < closest_distance:
                closest_distance = distance(reference[j], points[i])
                closest_point = j
        cluster_list[closest_point].append(points[i])

    return cluster_list

def k_means(k, points):
    # Performs the k-means clustering.
    reference_points = points[:k]  # our initial reference points

    # Using the reference points, cluster the points
    cluster_list1 = cluster(reference_points, points)

    # calculate the new reference points by finding the centroid of each cluster
    new_reference_points1 = []
    for i in cluster_list1:
        new_reference_points1.append(centroid(i))

    # re-cluster the points using the centroids
    cluster_list2 = cluster(new_reference_points1, points)

    # repeat until the centroids do not change between iterations.
    different = True
    cluster_list_final = []
    while different:
        new_reference_points2 = []
        for j in cluster_list2:
            new_reference_points2.append(centroid(j))
        if collections.Counter(new_reference_points2) == collections.Counter(new_reference_points1):
            cluster_list_final = cluster(new_reference_points2, points)
            different = False
        else:
            new_reference_points1 = new_reference_points2
            cluster_list2 = cluster(new_reference_points1, points)


    # return a list of lists of points representing the clusters.

    return cluster_list_final
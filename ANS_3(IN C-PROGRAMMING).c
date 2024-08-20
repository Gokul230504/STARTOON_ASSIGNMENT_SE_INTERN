#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 1000

typedef struct {
    int index;
    double value;
} Peak;

void find_peaks(double data[], int size, Peak maxima[], int *max_count, Peak minima[], int *min_count) {
    *max_count = 0;
    *min_count = 0;
    for (int i = 1; i < size - 1; i++) {
        if (data[i-1] < data[i] && data[i] > data[i+1]) {
            maxima[*max_count].index = i;
            maxima[*max_count].value = data[i];
            (*max_count)++;
        } else if (data[i-1] > data[i] && data[i] < data[i+1]) {
            minima[*min_count].index = i;
            minima[*min_count].value = data[i];
            (*min_count)++;
        }
    }
}

void print_peaks(Peak peaks[], int count, const char* peak_type) {
    printf("%s:\n", peak_type);
    for (int i = 0; i < count; i++) {
        printf("Index: %d, Value: %f\n", peaks[i].index, peaks[i].value);
    }
    printf("\n");
}

void process_data(const char* filename) {
    FILE *file;
    double data[MAX_SIZE];
    int size = 0;
    Peak maxima[MAX_SIZE], minima[MAX_SIZE];
    int max_count, min_count;

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file %s\n", filename);
        return;
    }

    while (fscanf(file, "%lf", &data[size]) != EOF && size < MAX_SIZE) {
        size++;
    }
    fclose(file);

    find_peaks(data, size, maxima, &max_count, minima, &min_count);

    printf("Results for %s:\n", filename);
    print_peaks(maxima, max_count, "Maxima");
    print_peaks(minima, min_count, "Minima");
}

int main() {
    process_data("Data_1.txt");
    process_data("Data_2.txt");
    return 0;
}
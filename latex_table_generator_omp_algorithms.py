
def get_execution_time_latex_table(algorithm_tag, results):
    data_rows = ""
    for precision_key in results.keys():
        times = list(results[precision_key].values())
        row = "\t" + str(precision_key)
        # Add blank spaces
        row += (8 - len(row)) * " "
        for time in times:
            string_time = f"& {time}"
            string_time += (12 - len(string_time)) * " "
            row += string_time
        row += "\\\\ \n\t\\hline \n"
        data_rows += row

    latex_table = "\\begin{table}[H]\n" \
                  "\\begin{center}\n" \
                  "\\large\n" \
                  "\\caption{Tiempos de ejecución (en segundos) del algoritmo " \
                  + algorithm_tag + \
                  " utilizando el paradigma de programación con OpenMP.}\n" \
                  "\\label{" \
                  f"table:ex-omp-{algorithm_tag.lower()}" \
                  "}\n" \
                  "\\begin{tabular}{| c | c | c | c | c | c | c | c |}\n" \
                  "\\hline\n" \
                  "\t\\multirow{2}{*}{\\textbf{Precisión}} & \multicolumn{7}{ | c | }{\\textbf{Número de hebras}} \\\\\n" \
                  "\t\\cline{2-8} & \\textbf{1} & \\textbf{2} & \\textbf{4} & \\textbf{8} & \\textbf{12} & \\textbf{16} & \\textbf{20} \\\\\n" \
                  "\t\\hline\n" \
                  + data_rows.replace('.', ',') + \
                  "\\end{tabular}\n" \
                  "\\end{center}\n" \
                  "\\end{table}\n"
    return latex_table


def get_speed_up_latex_table(algorithm_tag, results):
    data_rows = ""
    for precision_key in results.keys():
        times = list(results[precision_key].values())
        speed_ups = list()
        for i in range(len(times)):
            speed_ups.append(times[0] / times[i])
        row = "\t" + str(precision_key)
        # Add blank spaces
        row += (8 - len(row)) * " "
        for speed_up in speed_ups:
            string_su = f"& {speed_up}"
            string_su += (10 - len(string_su)) * " "
            row += string_su
        row += "\\\\ \n\t\\hline \n"
        data_rows += row

    latex_table = "\\begin{table}[H]\n" \
                  "\\begin{center}\n" \
                  "\\large\n" \
                  "\\caption{Escalabilidad del algoritmo " \
                  + algorithm_tag + \
                  " utilizando el paradigma de programación con OpenMP.}\n" \
                  "\\label{" \
                  f"table:su-omp-{algorithm_tag.lower()}" \
                  "}\n" \
                  "\\begin{tabular}{| c | c | c | c | c | c | c | c |}\n" \
                  "\\hline\n" \
                  "\t\\multirow{2}{*}{\\textbf{Precisión}} & \multicolumn{7}{ | c | }{\\textbf{Número de hebras}} \\\\\n" \
                  "\t\\cline{2-8} & \\textbf{1} & \\textbf{2} & \\textbf{4} & \\textbf{8} & \\textbf{12} & \\textbf{16} & \\textbf{20} \\\\\n" \
                  "\t\\hline\n" \
                  + data_rows.replace('.', ',') + \
                  "\\end{tabular}\n" \
                  "\\end{center}\n" \
                  "\\end{table}\n"
    return latex_table


if __name__ == '__main__':
    # Set file and path to store the plots
    results_path = 'results/omp/results-2022-12.csv'
    path_to_save = 'tables/omp/'

    data = load_results_from_file()

    for algorithm in data.keys():
        file = open(path_to_save + f"ex-{algorithm.lower()}.tex", "w")
        file.write(get_execution_time_latex_table(algorithm, data[algorithm]))
        file.close()
        file = open(path_to_save + f"su-{algorithm.lower()}.tex", "w")
        file.write(get_speed_up_latex_table(algorithm, data[algorithm]))
        file.close()

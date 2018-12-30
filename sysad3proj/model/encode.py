import functions as f
f.encode_numeric_zscore(df, 'duration')
f.encode_text_dummy(df, 'protocol_type')
f.encode_text_dummy(df, 'service')
f.encode_text_dummy(df, 'flag')
f.encode_numeric_zscore(df, 'src_bytes')
f.encode_numeric_zscore(df, 'dst_bytes')
f.encode_text_dummy(df, 'land')
f.encode_numeric_zscore(df, 'wrong_fragment')
f.encode_numeric_zscore(df, 'urgent')
f.encode_numeric_zscore(df, 'hot')
f.encode_numeric_zscore(df, 'num_failed_logins')
f.encode_text_dummy(df, 'logged_in')
f.encode_numeric_zscore(df, 'num_compromised')
f.encode_numeric_zscore(df, 'root_shell')
f.encode_numeric_zscore(df, 'su_attempted')
f.encode_numeric_zscore(df, 'num_root')
f.encode_numeric_zscore(df, 'num_file_creations')
f.encode_numeric_zscore(df, 'num_shells')
f.encode_numeric_zscore(df, 'num_access_files')
f.encode_numeric_zscore(df, 'num_outbound_cmds')
f.encode_text_dummy(df, 'is_host_login')
f.encode_text_dummy(df, 'is_guest_login')
f.encode_numeric_zscore(df, 'count')
f.encode_numeric_zscore(df, 'srv_count')
f.encode_numeric_zscore(df, 'serror_rate')
f.encode_numeric_zscore(df, 'srv_serror_rate')
f.encode_numeric_zscore(df, 'rerror_rate')
f.encode_numeric_zscore(df, 'srv_rerror_rate')
f.encode_numeric_zscore(df, 'same_srv_rate')
f.encode_numeric_zscore(df, 'diff_srv_rate')
f.encode_numeric_zscore(df, 'srv_diff_host_rate')
f.encode_numeric_zscore(df, 'dst_host_count')
f.encode_numeric_zscore(df, 'dst_host_srv_count')
f.encode_numeric_zscore(df, 'dst_host_same_srv_rate')
f.encode_numeric_zscore(df, 'dst_host_diff_srv_rate')
f.encode_numeric_zscore(df, 'dst_host_same_src_port_rate')
f.encode_numeric_zscore(df, 'dst_host_srv_diff_host_rate')
f.encode_numeric_zscore(df, 'dst_host_serror_rate')
f.encode_numeric_zscore(df, 'dst_host_srv_serror_rate')
f.encode_numeric_zscore(df, 'dst_host_rerror_rate')
f.encode_numeric_zscore(df, 'dst_host_srv_rerror_rate')
outcomes = f.encode_text_index(df, 'outcome')
num_classes = len(outcomes)

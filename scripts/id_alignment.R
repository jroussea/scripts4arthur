
alignment <- read.table("plouf.tsv", header = TRUE, sep = "\t")

id <- read.table("id_sequence.tsv", header = FALSE, sep = "\t")

df.tmp <- merge(id, alignment, by.x = "V1", by.y = "subject", all.y = TRUE)

df.tmp <- df.tmp %>% 
   select(-1) %>%
   rename(subject = "V2")
   

df.tmp.2 <- merge(id, df.tmp, by.x = "V1", by.y = "query",all.y = TRUE)

df.tmp.2 <- df.tmp.2 %>% 
   select(-1) %>%
   rename(query = "V2")

write.table(df.tmp.2, file = "plouf", sep = "\t", row.names = FALSE, col.names = TRUE)

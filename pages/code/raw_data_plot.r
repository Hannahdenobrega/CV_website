# Raw data not seasonally adjusted

library(pacman)
pacman::p_load(tidyverse, ggplot2, readr)

#setwd('/Users/hannahdenobrega/Documents/FoP_bin/pages')
setwd("./pages")

df <- read_csv("data/seasonal_data.csv")

plot_nsa <- df %>% mutate(value_sa = log(value_sa)) %>% 
  ggplot() + 
  #geom_line(aes(Date, seasonal_factor)) +
  geom_line(aes(Date, value), color = "steelblue") +
  # geom_line(aes(Date, value_sa)) +
  # facet_wrap(~ticker, scales = "free_y") + 
  ggthemes::theme_economist() + 
  ggthemes::scale_color_economist() + #theme_bw() + 
  labs(
    #x = "Date",
    x = "",
    y = "",
    #colour = "Fruit",
    title = "Fruit sales are highly seasonal"
    #title = ""
  ) +
  theme(
    plot.title = element_text(face = "bold", size = 12),
    legend.background = element_rect(fill = "white", size = 4, color = "white"),
    legend.justification = c(0, 1),
    legend.position = c(0, 1),
    axis.ticks = element_line(color = "grey70", size = 0.2),
    panel.grid.major = element_line(color = "grey70", size = 0.2),
    panel.grid.minor = element_blank(),
    panel.background = element_rect(fill='transparent')
  ) 

ggsave("plots/plot_nsa.png", width = 8, height = 6)
